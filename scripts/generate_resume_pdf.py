from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import wrap


PAGE_WIDTH = 612
PAGE_HEIGHT = 792
MARGIN_X = 54
TOP_Y = 752
CONTENT_WIDTH = PAGE_WIDTH - (MARGIN_X * 2)

ACCENT = (0.09, 0.18, 0.31)
TEXT = (0.08, 0.08, 0.08)
MUTED = (0.34, 0.38, 0.43)
RULE = (0.82, 0.84, 0.87)


@dataclass(frozen=True)
class ResumeContent:
    name: str
    title_line: str
    contact_lines: tuple[str, ...]
    summary: str
    role_heading: str
    role_meta: str
    experience_bullets: tuple[str, ...]
    education_lines: tuple[str, ...]
    project_entries: tuple[tuple[str, str], ...]
    skill_lines: tuple[str, ...]


CONTENT = ResumeContent(
    name="Nimish Sood",
    title_line="IT Support Specialist | Security Infrastructure | UPEI Computer Science (Co-op), Expected 2027",
    contact_lines=(
        "Prince Edward Island, Canada | vasusood889@gmail.com | github.com/NimishSood",
        "linkedin.com/in/nimishsood | nimishhomelab.com",
    ),
    summary=(
        "IT Support Specialist with hands-on experience across identity, endpoint, virtualization, "
        "and internal security operations. Complements professional infrastructure work with public "
        "security projects in Wazuh deployment and malicious URL classification, plus TryHackMe "
        "Pre Security completion and current SEC1 preparation."
    ),
    role_heading="AKA Energy Systems | IT Support Specialist",
    role_meta="Contract Full-time | Jul 2025 - Present | Prince Edward Island, Canada | On-site",
    experience_bullets=(
        "Supported core IT infrastructure and security operations across virtualized, server, identity, "
        "endpoint, and network environments.",
        "Implemented Microsoft Entra ID Conditional Access and built internal GoPhish campaigns for access "
        "control hardening and security awareness testing.",
        "Provisioned and managed Windows and Ubuntu virtual machines in Proxmox with static IP assignment, "
        "VLAN-aware configuration, and infrastructure support for internal services.",
        "Improved endpoint operations with ManageEngine Desktop Central for patching, software deployment, "
        "inventory management, and remote administration.",
        "Contributed to early planning for a Wazuh-based SIEM deployment to improve centralized logging, "
        "monitoring, and future detection capability.",
    ),
    education_lines=(
        "University of Prince Edward Island",
        "Bachelor of Science in Computer Science (Co-op) | Expected 2027",
    ),
    project_entries=(
        (
            "Wazuh Stack Bring-Up",
            "Deployed Wazuh indexer and dashboard on separate Ubuntu 24.04 VMs in VMware Workstation with TLS, "
            "JVM sizing, configuration notes, and documented verification steps.",
        ),
        (
            "Malicious URL Classification",
            "Built a lexical-feature benchmark with 651,191 source rows, 640,792 cleaned records, an "
            "80,000-row modeling sample, and saved binary and multiclass evaluation outputs.",
        ),
    ),
    skill_lines=(
        "Security / Identity: Microsoft Entra ID, Conditional Access, GoPhish, Wazuh, Pi-hole",
        "Infrastructure: Proxmox VE, VMware Workstation, Windows, Ubuntu, VLAN-aware networking",
        "Endpoint / Development: ManageEngine Desktop Central, Python, TypeScript, Git, Next.js, Firebase",
    ),
)


def pdf_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def fmt_color(color: tuple[float, float, float]) -> str:
    return " ".join(f"{channel:.3f}" for channel in color)


def wrap_for_width(text: str, width: float, font_size: float) -> list[str]:
    max_chars = max(18, int(width / (font_size * 0.51)))
    return wrap(text, width=max_chars, break_long_words=False, replace_whitespace=False)


class PDFCanvas:
    def __init__(self) -> None:
        self.commands: list[str] = []

    def draw_text(
        self,
        x: float,
        y: float,
        text: str,
        *,
        font: str = "F1",
        size: float = 11,
        color: tuple[float, float, float] = TEXT,
    ) -> None:
        self.commands.extend(
            [
                "BT",
                f"/{font} {size:.2f} Tf",
                f"{fmt_color(color)} rg",
                f"1 0 0 1 {x:.2f} {y:.2f} Tm",
                f"({pdf_escape(text)}) Tj",
                "ET",
            ]
        )

    def draw_rule(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        *,
        width: float = 1,
        color: tuple[float, float, float] = RULE,
    ) -> None:
        self.commands.extend(
            [
                f"{width:.2f} w",
                f"{fmt_color(color)} RG",
                f"{x1:.2f} {y1:.2f} m",
                f"{x2:.2f} {y2:.2f} l",
                "S",
            ]
        )

    def draw_paragraph(
        self,
        x: float,
        y: float,
        text: str,
        *,
        width: float,
        font: str = "F1",
        size: float = 10.5,
        color: tuple[float, float, float] = TEXT,
        leading: float | None = None,
    ) -> float:
        lines = wrap_for_width(text, width, size)
        line_height = leading or (size * 1.35)
        for line in lines:
            self.draw_text(x, y, line, font=font, size=size, color=color)
            y -= line_height
        return y

    def draw_bullet(
        self,
        x: float,
        y: float,
        text: str,
        *,
        width: float,
        size: float = 10.3,
        color: tuple[float, float, float] = TEXT,
    ) -> float:
        bullet_x = x
        text_x = x + 11
        wrapped = wrap_for_width(text, width - 11, size)
        line_height = size * 1.32
        for idx, line in enumerate(wrapped):
            if idx == 0:
                self.draw_text(bullet_x, y, "-", font="F1", size=size, color=color)
            self.draw_text(text_x, y, line, font="F1", size=size, color=color)
            y -= line_height
        return y - 4

    def render(self) -> bytes:
        return "\n".join(self.commands).encode("ascii")


def add_section_heading(canvas: PDFCanvas, y: float, title: str) -> float:
    canvas.draw_text(MARGIN_X, y, title.upper(), font="F2", size=10.5, color=ACCENT)
    canvas.draw_rule(MARGIN_X + 86, y + 4, PAGE_WIDTH - MARGIN_X, y + 4, width=0.8, color=RULE)
    return y - 20


def build_resume_pdf(output_path: Path) -> None:
    canvas = PDFCanvas()
    y = TOP_Y

    canvas.draw_text(MARGIN_X, y, CONTENT.name, font="F2", size=24, color=ACCENT)
    y -= 24
    canvas.draw_text(MARGIN_X, y, CONTENT.title_line, font="F1", size=11, color=TEXT)
    y -= 16
    for line in CONTENT.contact_lines:
        canvas.draw_text(MARGIN_X, y, line, font="F1", size=9.4, color=MUTED)
        y -= 12
    canvas.draw_rule(MARGIN_X, y + 2, PAGE_WIDTH - MARGIN_X, y + 2, width=1.0, color=RULE)

    y -= 22
    y = add_section_heading(canvas, y, "Summary")
    y = canvas.draw_paragraph(MARGIN_X, y, CONTENT.summary, width=CONTENT_WIDTH, size=10.5)

    y -= 8
    y = add_section_heading(canvas, y, "Experience")
    canvas.draw_text(MARGIN_X, y, CONTENT.role_heading, font="F2", size=11.4, color=TEXT)
    y -= 14
    canvas.draw_text(MARGIN_X, y, CONTENT.role_meta, font="F1", size=9.4, color=MUTED)
    y -= 18
    for bullet in CONTENT.experience_bullets:
        y = canvas.draw_bullet(MARGIN_X, y, bullet, width=CONTENT_WIDTH, size=10.2)

    y -= 4
    y = add_section_heading(canvas, y, "Projects")
    for title, description in CONTENT.project_entries:
        canvas.draw_text(MARGIN_X, y, title, font="F2", size=11.1, color=TEXT)
        y -= 14
        y = canvas.draw_bullet(MARGIN_X, y, description, width=CONTENT_WIDTH, size=10.15)
        y -= 2

    y = add_section_heading(canvas, y, "Education")
    canvas.draw_text(MARGIN_X, y, CONTENT.education_lines[0], font="F2", size=11.2, color=TEXT)
    y -= 14
    canvas.draw_text(MARGIN_X, y, CONTENT.education_lines[1], font="F1", size=10.2, color=MUTED)

    y -= 26
    y = add_section_heading(canvas, y, "Technical Skills")
    for skill_line in CONTENT.skill_lines:
        y = canvas.draw_paragraph(MARGIN_X, y, skill_line, width=CONTENT_WIDTH, size=10.1, color=TEXT)
        y -= 3

    if y < 52:
        raise RuntimeError(f"Resume content overflowed the page. Lowest y-position: {y:.2f}")

    content_stream = canvas.render()

    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Count 1 /Kids [3 0 R] >>",
        (
            b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            b"/Resources << /Font << /F1 4 0 R /F2 5 0 R >> >> "
            b"/Contents 6 0 R >>"
        ),
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>",
        b"<< /Length %d >>\nstream\n%s\nendstream" % (len(content_stream), content_stream),
    ]

    output = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for idx, obj in enumerate(objects, start=1):
        offsets.append(len(output))
        output.extend(f"{idx} 0 obj\n".encode("ascii"))
        output.extend(obj)
        output.extend(b"\nendobj\n")

    xref_offset = len(output)
    output.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    output.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        output.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    output.extend(
        (
            f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
            f"startxref\n{xref_offset}\n%%EOF"
        ).encode("ascii")
    )

    output_path.write_bytes(output)


if __name__ == "__main__":
    target = Path(__file__).resolve().parents[1] / "assets" / "Nimish-Sood-Resume.pdf"
    build_resume_pdf(target)
    print(f"Wrote {target}")

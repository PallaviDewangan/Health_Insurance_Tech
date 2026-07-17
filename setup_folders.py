#!/usr/bin/env python
"""
setup_folders.py
Helper script to initialize directory structures, Git keeps, and default
placeholder assets (using Pillow if installed) for the Guardian Health Insurance application.
Removes Unicode emojis from print statements to prevent encoding issues on Windows consoles.
"""

from pathlib import Path
import sys

def create_directory(path: Path) -> None:
    """Creates a directory if it does not exist, printing a success message."""
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        print(f"[OK] Created directory: {path}")
    else:
        print(f"[INFO] Directory already exists: {path}")

def create_gitkeep(directory: Path) -> None:
    """Creates a .gitkeep file inside the specified directory."""
    gitkeep_file = directory / ".gitkeep"
    if not gitkeep_file.exists():
        gitkeep_file.touch()
        print(f"[OK] Created .gitkeep inside: {directory}")
    else:
        print(f"[INFO] .gitkeep already exists in: {directory}")

def create_image_placeholder(filepath: Path, width: int, height: int, color: tuple, text: str) -> None:
    """
    Creates a placeholder PNG image using Pillow.
    If Pillow is not installed, creates an empty fallback file.
    """
    if filepath.exists():
        print(f"[INFO] Asset already exists: {filepath}")
        return

    try:
        from PIL import Image, ImageDraw, ImageFont
        # Create solid color image
        img = Image.new("RGBA", (width, height), color)
        draw = ImageDraw.Draw(img)

        # Draw a simple decorative background pattern/border
        draw.rectangle([0, 0, width - 1, height - 1], outline=(30, 136, 229, 255), width=3)

        # Simple text centering logic
        try:
            font = ImageFont.load_default()
        except IOError:
            font = None

        # Draw text centered (simple approximation)
        draw.text((width // 2 - (len(text) * 3), height // 2 - 5), text, fill=(255, 255, 255, 255), font=font)

        img.save(filepath, "PNG")
        print(f"[PAINT] Created decorative image placeholder: {filepath} ({width}x{height})")
    except ImportError:
        # Fallback to empty file if Pillow is not installed yet
        filepath.touch()
        print(f"[WARN] Pillow not installed. Created empty file placeholder: {filepath}")
    except Exception as e:
        # Prevent any unexpected crashes from interrupting setup
        filepath.touch()
        print(f"[WARN] Error creating PIL image: {e}. Created empty file placeholder: {filepath}")

def main() -> None:
    """Main execution function for folder setup."""
    print("--- Initializing Guardian Health Insurance File System Setup ---")
    
    # Establish base project directory path
    base_dir = Path(__file__).resolve().parent

    # Define directories to create
    directories = {
        "assets": base_dir / "assets",
        "reports": base_dir / "reports",
        "screenshots": base_dir / "screenshots",
        "docs": base_dir / "docs"
    }

    # 1. Create directories
    for dir_name, dir_path in directories.items():
        create_directory(dir_path)

    # 2. Create .gitkeeps for tracking empty directories in Git
    create_gitkeep(directories["reports"])
    create_gitkeep(directories["screenshots"])

    # 3. Create placeholder branding assets
    # Navy blue color for logo/banner backgrounds: (12, 35, 64)
    navy_color = (12, 35, 64, 255)
    light_grey_color = (200, 200, 200, 255)

    create_image_placeholder(
        filepath=directories["assets"] / "logo.png",
        width=200,
        height=200,
        color=navy_color,
        text="Guardian Logo"
    )

    create_image_placeholder(
        filepath=directories["assets"] / "banner.png",
        width=1200,
        height=400,
        color=navy_color,
        text="Guardian Health Insurance Banner"
    )

    create_image_placeholder(
        filepath=directories["assets"] / "avatar.png",
        width=100,
        height=100,
        color=light_grey_color,
        text="User Profile"
    )

    print("\n[OK] Setup complete! Project directories and assets are ready.")

if __name__ == "__main__":
    main()

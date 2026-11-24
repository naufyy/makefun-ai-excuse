"""Write a fixed one-line AI excuse to /output/entry.txt (deterministic, no network)."""
import os

ENTRY = (
    "I did not take down production. I deployed at 2am, watched every dashboard turn red, "
    "and assumed it was a festive theme."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

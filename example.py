from main import detect_from_text, detect_from_html
import example_data


def solve(data, content_type):
    if content_type == "html":
        return detect_from_html(data)
    return detect_from_text(data)


if __name__ == "__main__":
    from_text = solve(example_data.FIRST_DATA, content_type="text")
    from_html = solve(example_data.SECOND_DATA, content_type="html")

    print(f"DETECT FROM TEXT: {from_text}")
    print(f"\nDETECT FROM HTML: {from_html}")

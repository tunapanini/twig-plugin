def on_content_change(html, *args, **kwargs):
    """Called when the content of the note changes

    Args:
        html: The HTML content of the note
    """
    print("Content changed!")
    # TODO: Do something with the content
    return html  # Return the modified HTML
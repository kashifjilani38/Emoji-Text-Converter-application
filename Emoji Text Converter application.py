# ============================================================
# Professional Emoji Text Converter
# Gradio 6.x Compatible
# ============================================================

import demoji
import gradio as gr


# ============================================================
# Emoji Processing Functions
# ============================================================

def remove_emojis(text):
    """Remove emojis from text."""
    if not text:
        return ""

    return demoji.replace(text, "")


def emoji_to_text(text):
    """Convert emojis into text descriptions."""
    if not text:
        return ""

    return demoji.replace_with_desc(text)


def find_emojis(text):
    """Find all emojis in the text."""
    if not text:
        return "No text provided."

    emojis = demoji.findall(text)

    if not emojis:
        return "No emojis found."

    results = []

    for emoji, description in emojis.items():
        results.append(f"{emoji}  →  {description}")

    return "\n".join(results)


def analyze_text(text):
    """Analyze text and return statistics."""

    if not text:
        return "No text provided."

    emojis = demoji.findall(text)

    character_count = len(text)
    word_count = len(text.split())
    emoji_count = len(emojis)

    if emojis:
        emoji_list = ", ".join(emojis.keys())
    else:
        emoji_list = "None"

    return (
        "📊 TEXT ANALYSIS\n"
        "══════════════════════════════\n\n"
        f"Characters : {character_count}\n"
        f"Words      : {word_count}\n"
        f"Emojis     : {emoji_count}\n\n"
        "Detected Emojis\n"
        "──────────────────────────────\n"
        f"{emoji_list}"
    )


# ============================================================
# Main Processing Function
# ============================================================

def process_text(text, operation):

    if not text or not text.strip():
        return "⚠️ Please enter some text first."

    try:

        if operation == "🗑️ Remove Emojis":
            return remove_emojis(text)

        elif operation == "🔤 Convert Emojis to Text":
            return emoji_to_text(text)

        elif operation == "🔎 Find Emojis":
            return find_emojis(text)

        elif operation == "📊 Analyze Text":
            return analyze_text(text)

        return text

    except Exception as error:
        return f"❌ Error: {error}"


# ============================================================
# Example Text
# ============================================================

example_text = """Good morning! ☀️🌸😊
Welcome to our party! 🎉🥳
Happy birthday! 🎂🎈
Have a wonderful day! ❤️"""


# ============================================================
# User Interface
# ============================================================

with gr.Blocks(
    title="Emoji Text Converter"
) as app:

    # --------------------------------------------------------
    # Header
    # --------------------------------------------------------

    gr.Markdown(
        """
        # 😀 Emoji Text Converter

        ### Professional Emoji Processing Tool

        Convert, remove, detect, and analyze emojis from your text.

        ---
        """
    )

    # --------------------------------------------------------
    # Main Layout
    # --------------------------------------------------------

    with gr.Row():

        # ====================================================
        # INPUT PANEL
        # ====================================================

        with gr.Column():

            gr.Markdown("### 📝 Input")

            input_text = gr.Textbox(
                label="Enter Your Text",
                placeholder="Type or paste your text here...",
                value=example_text,
                lines=12
            )

            operation = gr.Radio(
                choices=[
                    "🗑️ Remove Emojis",
                    "🔤 Convert Emojis to Text",
                    "🔎 Find Emojis",
                    "📊 Analyze Text"
                ],
                value="🔤 Convert Emojis to Text",
                label="Processing Mode"
            )

            with gr.Row():

                process_button = gr.Button(
                    "🚀 Process",
                    variant="primary"
                )

                clear_button = gr.Button(
                    "🧹 Clear"
                )

        # ====================================================
        # OUTPUT PANEL
        # ====================================================

        with gr.Column():

            gr.Markdown("### 📤 Output")

            output_text = gr.Textbox(
                label="Result",
                lines=12,
                interactive=False
            )

            copy_button = gr.Button(
                "📋 Copy Result"
            )

    # --------------------------------------------------------
    # Examples
    # --------------------------------------------------------

    gr.Markdown(
        """
        ---
        ### 💡 Example Text
        """
    )

    gr.Examples(
        examples=[
            ["Good morning! ☀️🌸😊"],
            ["Happy birthday! 🎂🎈🥳"],
            ["Welcome to the party! 🎉🎊🍕"],
            ["I love Python! 🐍❤️🔥"],
            ["Congratulations! 🎉🏆👏😊"],
            ["Have a wonderful day! 🌞🌻❤️"]
        ],
        inputs=input_text
    )

    # --------------------------------------------------------
    # Information
    # --------------------------------------------------------

    with gr.Accordion("ℹ️ About this application", open=False):

        gr.Markdown(
            """
            **Emoji Text Converter** is a Python application for
            processing Unicode emojis.

            **Features:**

            - 🗑️ Remove emojis
            - 🔤 Convert emojis to descriptions
            - 🔎 Detect emojis
            - 📊 Analyze text
            - 📋 Copy results
            - 💡 Built-in examples

            **Technologies:**

            - Python
            - Demoji
            - Gradio
            """
        )

    # --------------------------------------------------------
    # Event Handlers
    # --------------------------------------------------------

    process_button.click(
        fn=process_text,
        inputs=[input_text, operation],
        outputs=output_text
    )

    operation.change(
        fn=process_text,
        inputs=[input_text, operation],
        outputs=output_text
    )

    clear_button.click(
        fn=lambda: ("", ""),
        inputs=None,
        outputs=[input_text, output_text]
    )


# ============================================================
# Launch Application
# ============================================================

if __name__ == "__main__":

    app.launch(
        theme=gr.themes.Soft(),
        inbrowser=True
    )
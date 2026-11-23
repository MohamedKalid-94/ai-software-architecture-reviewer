class TextProcessingService:


    def normalize_text(
        self,
        text
    ):

        text = text.replace(
            "\n\n",
            "\n"
        )


        text = text.strip()


        return text
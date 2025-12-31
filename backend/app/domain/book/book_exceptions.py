class BookDomainException(Exception):
    """Base book domain error"""
    code: str = "business_rule_violation"
    fields: dict[str, str] | None = None

    def __init__(
        self,
        message: str | None = None,
        *,
        fields: dict[str, str] | None = None,
    ):
        super().__init__(message)
        self.message = message
        self.fields = fields

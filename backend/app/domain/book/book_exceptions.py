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


# ------------------
# --- Isbn Error ---
# ------------------

class IsbnAlreadyExist(BookDomainException):
    pass


class IsbnIsBlankError(BookDomainException):
    pass


class InvalidIsbnError(BookDomainException):
    pass


# -------------------
# --- Title Error ---
# -------------------

class TitleIsBlankError(BookDomainException):
    pass


class TitleTooShortError(BookDomainException):
    pass


class TitleTooLongError(BookDomainException):
    pass


# --------------------
# --- Author Error ---
# --------------------

class AuthorIsBlankError(BookDomainException):
    pass


class AuthorTooShortError(BookDomainException):
    pass


class AuthorTooLongError(BookDomainException):
    pass


# -------------------
# --- Pages Error ---
# -------------------

class PagesTooLowError(BookDomainException):
    pass


class PagesTooHighError(BookDomainException):
    pass


# ----------------------
# --- Language Error ---
# ----------------------

class LanguageIsBlankError(BookDomainException):
    pass


class LanguageTooShortError(BookDomainException):
    pass


class LanguageTooLongError(BookDomainException):
    pass


# ------------------
# --- Year Error ---
# ------------------

class YearTooLowError(BookDomainException):
    pass


class YearTooHighError(BookDomainException):
    pass


# -------------------------
# --- Description Error ---
# -------------------------

class DescriptionTooLongError(BookDomainException):
    pass

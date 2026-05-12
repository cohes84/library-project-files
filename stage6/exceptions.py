class LibraryError(Exception):
    pass

class BookNotAvailableError(LibraryError):
    pass

class BookNotFoundError(LibraryError):
    pass

class MemberNotFoundError(LibraryError):
    pass

class InvalidMemberIDError(LibraryError):
    pass
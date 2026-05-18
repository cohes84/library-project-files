class LibraryError(Exception):
    pass

class BookNotFoundError(LibraryError):
    pass

class BookNotAvailableError(LibraryError):
    pass

class BookAlreadyExistsError(LibraryError):
    pass

class BookAvailableError(LibraryError):
    pass

class MemberNotFoundError(LibraryError):
    pass

class MemberAlreadyExistsError(LibraryError):
    pass

class InvalidMemberIDError(LibraryError):
    pass

class LoanNotFoundError(LibraryError):
    pass
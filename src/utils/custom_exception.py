import sys

class CustomException(Exception):
    """Base class for custom exceptions in the project."""
    def __init__(self, message:str, error_detail: Exception = None):
        self.error_message = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message: str, error_detail: Exception) -> str:
        """Constructs a detailed error message including the file name and line number."""
        _, _, tb = sys.exc_info()
        line_number = tb.tb_lineno if tb else 'Unknown Line'
        file_name = tb.tb_frame.f_code.co_filename if tb else 'Unknown File'
        return f"{message} | Error: {error_detail} | File: {file_name} | Line: {line_number}"
    
    def __str__(self):
        return self.error_message
    

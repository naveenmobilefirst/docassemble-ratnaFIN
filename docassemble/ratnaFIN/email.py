from docassemble.base.util import CustomDataType, DAValidationError
import re

class Email(CustomDataType):
    name = 'email'
    container_class = 'da-email-container'
    input_class = 'da-email'
    javascript = """\
$.validator.addMethod('email', function(value, element, params){
  return value == '' || /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$/.test(value);
});
"""
    jq_rule = 'email'
    jq_message = 'You need to enter a valid email address.'
    
    @classmethod
    def validate(cls, item):
        item = str(item).strip()
        if item == '' or re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', item):
            return True
        raise DAValidationError("Invalid email address format")
    
    @classmethod
    def transform(cls, item):
        return str(item).strip()

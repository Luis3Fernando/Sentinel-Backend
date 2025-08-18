class StandardResponseMixin:
    def standard_response(self, data=None, messages=None, status_type="success"):
        return {
            "type": status_type,
            "dto": data if data is not None else [],
            "listMessage": messages if messages is not None else [],
        }

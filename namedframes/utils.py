class ValidateMixIn:
    def _validate(self):
        missing_columns = []
        for column_name, column_type in self.__annotations__.items():
            if column_name not in self.columns:
                missing_columns.append((column_name, column_type))
        if missing_columns:
            raise ValueError(f"missing columns: {missing_columns}")

class ReprMixIn:
    def _repr_alt(self):
        message = "DataFrame with columns:\n"
        column_descriptions = [
            f"{column_name}: {column_type}"
            for column_name, column_type in self.__annotations__.items()
        ]
        message += "\n".join(column_descriptions)
        return message + "\n" + super().__repr__()

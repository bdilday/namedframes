class ValidateMixIn:
    def _validate(self):
        missing_columns = []
        for column_name, column_type in self.__annotations__.items():
            if column_name not in self.columns:
                missing_columns.append((column_name, column_type))
        if missing_columns:
            raise ValueError(f"missing columns: {missing_columns}")

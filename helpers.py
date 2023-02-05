class DictRetriever:
    RESULT = []

    @staticmethod
    def __retrieve(key, element):
        if isinstance(element, dict):
            if element.get(key) is not None:
                found_key = element.get(key, None)
                DictRetriever.RESULT.append(found_key)
            else:
                for sub_key in element:
                    DictRetriever.__retrieve(key, element[sub_key])
        elif isinstance(element, list):
            for sub_element in element:
                DictRetriever.__retrieve(key, sub_element)
    
    @staticmethod
    def get_nested_key(key, element):
        DictRetriever.RESULT = []
        DictRetriever.__retrieve(key, element)
        return DictRetriever.RESULT
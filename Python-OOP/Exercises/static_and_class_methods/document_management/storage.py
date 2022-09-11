class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        storage_category = self.__find_item_by_id(category.id, self.categories)
        if storage_category is None:
            self.categories.append(category)

    def add_topic(self, topic):
        storage_topic = self.__find_item_by_id(topic.id, self.topics)
        if storage_topic is None:
            self.topics.append(topic)

    def add_document(self, document):
        storage_document = self.__find_item_by_id(document.id, self.documents)
        if storage_document is None:
            self.documents.append(document)

    def __find_item_by_id(self, item_id, location):
        for item in location:
            if item.id == item_id:
                return item

    def edit_category(self, category_id, new_name):
        category = self.__find_item_by_id(category_id, self.categories)
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.__find_item_by_id(topic_id, self.topics)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = self.__find_item_by_id(document_id, self.documents)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.__find_item_by_id(category_id, self.categories)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__find_item_by_id(topic_id, self.topics)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__find_item_by_id(document_id, self.documents)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.__find_item_by_id(document_id, self.documents)
        return document

    def __repr__(self):
        return '\n'.join([repr(x) for x in self.documents])


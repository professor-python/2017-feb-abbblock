
# Синглтон = Одиночка (шаблон проектирования)

# + всегда один экземпляр
# - ( плох для потоков )


class SomeClass:

    __instance = None

    @staticmethod
    def get_instance():
        if not SomeClass.__instance:
            SomeClass.__instance = SomeClass()
        return SomeClass.__instance


obj_1 = SomeClass.get_instance()
obj_2 = SomeClass.get_instance()

print(obj_1 is obj_2)


# 4. порпобуйте Config сделать Одиночкой


from abc import ABCMeta, abstractmethod


class Animal:

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def unexecute(self):
        pass


class Duck(Animal):

    def execute(self):
        return 'KRYA-KRYA...'

    def unexecute(self):
        return 'stop KRYA-KRYA'

class Dog(Animal):

    def execute(self):
        return 'ГАВ-ГАВ...'

    def unexecute(self):
        return 'stop ГАВ-ГАВ'

class Python(Animal):

    def execute(self):
        return 'sch-sch-sch...'

    def unexecute(self):
        return 'stop sch-sch-sch'


if __name__=='__main__':

    from unittest import TestCase, main

    class SimpleTest(TestCase):

        def test_all(self):

            animals = [
                Dog(),
                Duck(),
                Python()
            ]
            out = [ a.execute() for a in animals ]
            out += [ a.unexecute() for a in animals ]

            #print(out)

            self.assertEqual(
                ['ГАВ-ГАВ...', 'KRYA-KRYA...', 'sch-sch-sch...', 'stop ГАВ-ГАВ', 'stop KRYA-KRYA', 'stop sch-sch-sch'],
                out
            )

    main()


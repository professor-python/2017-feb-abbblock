

# Действительная защита аттрибутов
# getattr и setattr

class A:

    def _method(self):
        pass

    def __method2(self):
        pass


class B:

    def __getattr__(self, name):
        if name == 'car':
            return 'car-car'
        return None
        #raise Exception('no attr {}'.format(name))


class StudentIvan:

    # age = 200
    not_none = True

    # для отсутствующих аттрибутов:
    def __getattr__(self, name):
        if name == 'age':
            return 20
        if name == 'name':
            return 'Ivan'

    def __setattr__(self, name, value):
        pass


if __name__=='__main__':

    from unittest import TestCase, main

    class SimpleTest(TestCase):

        def test_one(self):
            b = B()

            self.assertEqual( None, b.vbfhdjvb )
            self.assertEqual( None, b.Hello )
            self.assertEqual( None, b.plus_1 )

        def test_two(self):
            self.assertEqual( 'car-car', B().car )

        def test_three(self):
            self.assertEqual('Ivan', StudentIvan().name)
            self.assertEqual(20, StudentIvan().age)
            self.assertEqual(None, StudentIvan().vbfdg67bg76)
            self.assertEqual(True, StudentIvan().not_none)

        def test_4(self):
            stud = StudentIvan()
            stud.work = 'good'
            self.assertEqual(None, stud.work)

    main()


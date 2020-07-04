#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class FixTogether(AnyObject):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FixTogether
                | 
                | The object that manages a sequence of products or
                | fixTogethers.
                | 
                | It belongs to the FixTogether collection of a Product.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.fix_together = com_object

    @property
    def fix_togethers_count(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FixTogethersCount() As long (Read Only)
                | 
                |     Returns the number of FixTogether entities in the
                |     FixTogether.
                | 
                |     Example:
                |         The following example retrieves in fixTogethersCount the number of
                |         FixTogethers of the myFixTogether FixTogether :
                | 
                |          fixTogethersCount = myFixTogether.FixTogethersCount

        :return: int
        """

        return self.fix_together.FixTogethersCount

    @property
    def products_count(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ProductsCount() As long (Read Only)
                | 
                |     Returns the number of products fixed together in the
                |     FixTogether.
                | 
                |     Example:
                |         The following example retrieves in productsCount the number of products
                |         of the myFixTogether FixTogether :
                | 
                |          productsCount = myFixTogether.ProductsCount

        :return: int
        """

        return self.fix_together.ProductsCount

    def add_fix_together(self, i_fix_together=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddFixTogether(FixTogether iFixTogether)
                | 
                |     Add a fixTogether to a FixTogether. The fixTogether is fixed together with
                |     the products or fixTogethers already contained in the FixTogether.
                |     
                | Example:
                |     The following example adds a FixTogether fixTogether in a FixTogether
                |     myFixTogether.
                | 
                |      myFixTogether.AddFixTogether(fixTogether)

        :param FixTogether i_fix_together:
        :return: None
        """
        return self.fix_together.AddFixTogether(i_fix_together.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_fix_together'
        # # vba_code = """
        # # Public Function add_fix_together(fix_together)
        # #     Dim iFixTogether (2)
        # #     fix_together.AddFixTogether iFixTogether
        # #     add_fix_together = iFixTogether
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_product(self, i_product=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddProduct(Product iProduct)
                | 
                |     Add a product to a FixTogether. The product is fixed together with the
                |     products and fixTogethers already contained in the FixTogether.
                |     
                | Example:
                |     The following example adds a Product myProduct in a
                |     FixTogether.
                | 
                |      myFixTogether.AddProduct(myProduct)

        :param Product i_product:
        :return: None
        """
        return self.fix_together.AddProduct(i_product.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_product'
        # # vba_code = """
        # # Public Function add_product(fix_together)
        # #     Dim iProduct (2)
        # #     fix_together.AddProduct iProduct
        # #     add_product = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_fix_together(self, i_index=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetFixTogether(CATVariant iIndex) As FixTogether
                | 
                |     Returns a FixTogether using its index or its name in the
                |     FixTogether.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the FixTogether to retrieve. As a
                |             numerics, this index is the rank of the FixTogether in the FixTogethers of the
                |             FixTogether. The index of the first FixTogether is 1, and the index of the last
                |             FixTogether is FixTogethersCount. As a string, it is the name you assigned to
                |             the FixTogether using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved FixTogether 
                |     Example:
                |         This example retrieves in thisFixTogether the fifth FixTogether and in
                |         thatFixTogether the FixTogether named myFixTogether in the FixTogethers of the
                |         FixTogether.
                | 
                |          Dim thisFixTogether As FixTogether
                |          Set thisFixTogether = myFixTogether.GetFixTogether(5)
                |          Dim thatFixTogether As FixTogether
                |          Set thatFixTogether = myFixTogether.GetFixTogether("myFixTogether")

        :param CATVariant i_index:
        :return: FixTogether
        """
        return FixTogether(self.fix_together.GetFixTogether(i_index.com_object))

    def get_product(self, i_index=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetProduct(CATVariant iIndex) As Product
                | 
                |     Returns a Product using its index or its name in the
                |     FixTogether.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Product to retrieve. As a numerics,
                |             this index is the rank of the Product in the products of the FixTogether. The
                |             index of the first Product is 1, and the index of the last Product is
                |             ProductsCount. As a string, it is the name you assigned to the Product using
                |             the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved Product 
                |     Example:
                |         This example retrieves in thisProduct the fifth Product and in
                |         thatProduct the Product named myProduct in the products of the
                |         FixTogether.
                | 
                |          Dim thisProduct As Product
                |          Set thisProduct = myFixTogether.GetProduct(5)
                |          Dim thatProduct As Product
                |          Set thatProduct = myFixTogether.GetProduct("myProduct")

        :param CATVariant i_index:
        :return: Product
        """
        return Product(self.fix_together.GetProduct(i_index.com_object))

    def remove_fix_together(self, i_index=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveFixTogether(CATVariant iIndex)
                | 
                |     Removes a FixTogether from the FixTogether.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the FixTogether to remove from the
                |             FixTogether. As a numerics, this index is the rank of the FixTogether in the
                |             FixTogethers of the FixTogether. The index of the first FixTogether is 1, and
                |             the index of the last FixTogether is FixTogethersCount. As a string, it is the
                |             name you assigned to the FixTogether using the 
                | 
                |         AnyObject.Name property. 
                | 
                | Example:
                |     This example removes the last FixTogether of the
                |     FixTogether.
                | 
                |     fixTogether.RemoveFixTogether(fixTogether.FixTogethersCount)

        :param CATVariant i_index:
        :return: None
        """
        return self.fix_together.RemoveFixTogether(i_index.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_fix_together'
        # # vba_code = """
        # # Public Function remove_fix_together(fix_together)
        # #     Dim iIndex (2)
        # #     fix_together.RemoveFixTogether iIndex
        # #     remove_fix_together = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_product(self, i_index=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveProduct(CATVariant iIndex)
                | 
                |     Removes a Product from the FixTogether.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Product to remove from the
                |             FixTogether. As a numerics, this index is the rank of the Product in the
                |             products of the FixTogether. The index of the first Product is 1, and the index
                |             of the last Product is ProductsCount. As a string, it is the name you assigned
                |             to the FixTogether using the 
                | 
                |         AnyObject.Name property. 
                | 
                | Example:
                |     This example removes the last Product of the FixTogether.
                | 
                |      fixTogether.RemoveProduct(fixTogether.ProductsCount)

        :param CATVariant i_index:
        :return: None
        """
        return self.fix_together.RemoveProduct(i_index.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_product'
        # # vba_code = """
        # # Public Function remove_product(fix_together)
        # #     Dim iIndex (2)
        # #     fix_together.RemoveProduct iIndex
        # #     remove_product = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'FixTogether(name="{self.name}")'
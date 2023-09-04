class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Si la lista no contiene valores, retorna vacío
        if not nums:
            print("La lista está vacía")

        # Iteramos sobre la lista en busca de un número repetido
        for num in nums:
            if nums.count(num) > 1: #Contamos cuántas veces está el número en el cual nos encontramos y si está + de 1 vez, lo eliminamos
                nums.remove(num)
                
        return sorted(nums) # Retornamos la lista ordenada

#Ejemplo

#Instanciación de la clase
solution = Solution()
lista = [1, 2, 3, 3, 4, 5, 1, 2] # Lista para testeo
print(solution.removeDuplicates(lista)) # Llamamos la función
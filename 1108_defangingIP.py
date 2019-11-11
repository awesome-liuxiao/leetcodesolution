class Solution:
    def defangIPaddr(self, address: str) -> str:
        if address == "":
            return address
        address = address.replace(".", "[.]")

        # print(address)
        return address

x = Solution()

address = "1.1.1.1"
x.defangIPaddr(address)

address = "255.100.50.0"
x.defangIPaddr(address)
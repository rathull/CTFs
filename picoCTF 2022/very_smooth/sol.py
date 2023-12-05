# Stuff for dividing large numbers - https://www.playandlearntocode.com/article/integer-division-algorithm-python-leetcode
class Solution:
    MIN_INT = pow(-2, 31)
    MAX_INT = pow(2, 31) - 1

    def recursive_divide(self, current_dividend: int, current_divisor: int):
        quotient = 1
        accumulator = current_divisor  # same as current_divisor * quotient because quotient == 1 at this point
        # base case
        if current_dividend < current_divisor:
            return 0
        elif current_dividend == current_divisor:
            return 1

        while accumulator < current_dividend:
            quotient = quotient << 1
            accumulator = accumulator << 1  # implicit quotient inclusion here!

        # undo the last step, because accumulator is now larger than current_dividend
        accumulator = accumulator >> 1
        quotient = quotient >> 1
        return quotient + self.recursive_divide(current_dividend - accumulator, current_divisor)

    def divide(self, dividend: int, divisor: int) -> int:
        '''
        Main method of this module.
        :param dividend:
        :param divisor:
        :return:
        '''
        # determine the sign of quotient:
        negative = False
        if (dividend >= 0 and divisor >= 0):
            negative = False
        elif (dividend < 0 and divisor >= 0):
            negative = True
        elif (dividend > 0 and divisor <= 0):
            negative = True

        # extract positive values of dividend and divisor:
        abs_dividend, abs_divisor = abs(dividend), abs(divisor)

        # watch for limits:
        if (abs_divisor == 1):
            if (negative == True):
                return -abs_dividend if Solution.MIN_INT < -abs_dividend else Solution.MIN_INT
            else:
                return abs_dividend if Solution.MAX_INT > abs_dividend else Solution.MAX_INT

        q = self.recursive_divide(abs_dividend, abs_divisor)
        return q if negative == False else -q

n = 0xc5261293c8f9c420bc5291ac0c14e103944b6621bb2595089f1641d85c4dae589f101e0962fe2b25fcf4186fb259cbd88154b75f327d990a76351a03ac0185af4e1a127b708348db59cd4625b40d4e161d17b8ead6944148e9582985bbc6a7eaf9916cb138706ce293232378ebd8f95c3f4db6c8a77a597974848d695d774efae5bd3b32c64c72bcf19d3b181c2046e194212696ec41f0671314f506c27a2ecfd48313e371b0ae731026d6951f6e39dc6592ebd1e60b845253f8cd6b0497f0139e8a16d9e5c446e4a33811f3e8a918c6cd917ca83408b323ce299d1ea9f7e7e1408e724679725688c92ca96b84b0c94ce717a54c470d035764bc0b92f404f1f5
c = 0x1f511af6dd19a480eb16415a54c122d7485de4d933e0aeee6e9b5598a8e338c2b29583aee80c241116bc949980e1310649216c4afa97c212fb3eba87d2b3a428c4cc145136eff7b902c508cb871dcd326332d75b6176a5a551840ba3c76cf4ad6e3fdbba0d031159ef60b59a1c6f4d87d90623e5fe140b9f56a2ebc4c87ee7b708f188742732ff2c09b175f4703960f2c29abccf428b3326d0bd3d737343e699a788398e1a623a8bd13828ef5483c82e19f31dca2a7effe5b1f8dc8a81a5ce873a082016b1f510f712ae2fa58ecdd49ab3a489c8a86e2bb088a85262d791af313b0383a56f14ddbb85cb89fb31f863923377771d3e73788560c9ced7b188ba97

# Use pollard.py to find p
p = 159652342260602436611264882107764540496206777532515381978886917602247902747922672308128228056532167311635408138845484288179466203049041882723045592330122232567342518194630068422135188545880928509542459095514667379085548962076958641693004621121073173222707331672786582779407036356311260724097659870075337003627
q = Solution.divide(Solution(), n, p)

# Standard RSA decrypting
e = 65537
phi = (p-1) * (q-1)
d = pow(e, -1, phi)
m = pow(c, d, n)
print(
    bytes.fromhex(
        hex(m)[2:]
    ).decode('ASCII')  
)
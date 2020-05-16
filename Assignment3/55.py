class Conversion:
    def kilosToPounds(self,kilo):
        assert(kilo<100), "Weight more than 100 kilograms"
        assert(kilo>0), "Negative value"
        return kilo*2.2
if __name__ =="__main__":
    obj1 = Conversion()
    val1 = obj1.kilosToPounds(10); print val1
    val2 = obj1.kilosToPounds(-3); print val2
    val3 = obj1.kilosToPounds(123); print val3

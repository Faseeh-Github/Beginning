Mercury={"Distance from Sun":"64.618 million km","Distance from Earth":"77 million km","Location":"Firstplanet in non habitable zone",
         "Planet type":"Rocky","Spin":"Counter clockwise","Surface temperature":"430 degrees Celsius",
         "Magnetic feild":"weaker than earth","Number of Moons":"Zero","Gravity":"3.7 m/s²","Mass":"3.285 × 10^23 kg",
         "Diameter":"4,879.4 km","Orbital Period":"88 days","Rotational period":"59d 0h 0m","Life":"No life","Atmosphere":"No atmosphere",
         "Rings":"No rings"}

Venus= {"Distance from Sun":"108.83 million km","Distance from Earth":"61 million kilometers","Location":"Second Planet in non habitable zone",
         "Planet type":"Rocky","Spin":"Clockwise","Surface temperature":"475 degrees Celsius",
         "Magnetic feild":"No magnetic feild","Number of Moons":"Zero","Gravity":"8.87 m/s²","Mass":"4.867 × 10^24 kg",
         "Diameter":"12,104 km","Orbital Period":"225 days","Rotational period":"243d 0h 0m","Life":"Maybe.To date no definative evidence","Atmosphere":"Thick toxic atmosphere filled with Carbon dioxide",
         "Rings":"No rings"}

Earth=  {"Distance from Sun":"151.14 million km","Location":"Third planet in habitable zone",
         "Planet type":"Rocky","Spin":"Counter Clockwise","Surface temperature":"13.9 degrees Celsius",
         "Magnetic feild":"Strong magnetic fild","Number of Moons":"1","Gravity":"9.8 m/s²","Mass":"5.97219 × 1024 kilograms",
         "Diameter":"12,742 km","Orbital Period":"365 days","Rotational period":"24 hours","Life":"Only planet in solar system that has life Maybe the only in universe having 8.7 million species","Atmosphere":"Have strong atmosphere mainly compose of Nitrogen, Oxygen and other gases",
         "Rings":"No rings"}

Mars =  {"Distance from Sun":"244.94 million km","Distance from Earth":"140 million miles","Location":"4th planet in habitable zone",
         "Planet type":"Rocky","Spin":"Counter Clockwise","Surface temperature":"20 degrees Celsius",
         "Magnetic feild":"Have magnetic feild","Number of Moons":"2(Phobos and Deimos)","Gravity":"3.71 m/s²","Mass":"6.39 × 10^23 kg",
         "Diameter":"6,779 km","Orbital Period":"687 days","Rotational period":"1d 0h 37m","Life":"Maybe.To date no definative evidence","Atmosphere":"Thin atmosphere mostly made of Carbon dioxide,Argon,Nitrogen and other gases",
         "Rings":"No rings"}

Jupiter= {"Distance from Sun":"778 million km","Distance from Earth":"679.26 million km","Location":"5th planet in non habitable zone",
         "Planet type":"Gas gaint","Spin":"Counter Clockwise","Surface temperature":"No any solid surface",
         "Magnetic feild":"Have magnetic feild and @0mtimes stronger than Earth","Number of Moons":"95","Gravity":"24.79 m/s²","Mass":"1.898 × 10^27 kg",
         "Diameter":"139,820 km biggest planet in the solar system","Orbital Period":"12 years","Rotational period":"0d 9h 56m","Life":"No life","Atmosphere":"Largest planetary atmosphere in the solar system mostly contain molecular Hydrogen and Helium",
         "Rings":"Have rings but very thin"}

Saturn = {"Distance from Sun":"1.4604 billion km","Distance from Earth":"1.3093 billion km","Location":"6th planet in non habitable zone",
         "Planet type":"Gas gaint","Spin":"Counter Clockwise","Surface temperature":"No any solid surface but it is a cool planet",
         "Magnetic feild":"Slightly weaker than Earth","Number of Moons":"145","Gravity":"10.44 m/s²","Mass":"5.683 × 10^26 kg",
         "Diameter":"116 464 kilometers","Orbital Period":"29 years","Rotational period":"0d 10h 34m","Life":"No life","Atmosphere":"Its solar system mostly contain molecular Hydrogen and Helium",
         "Rings":"Very beautifull,thick and biggest rings in entire solar system"}

Uranus = {"Distance from Sun":"2.936 billion km","Distance from Earth":"2.6 billion kilometers","Location":"7th planet in non habitable zone",
         "Planet type":"Gas gaint","Spin":"Clockwise","Surface temperature":"No any solid surface but it is too much cool planet",
         "Magnetic feild":" In some places in the southern hemisphere of Uranus the magnetic field is only 1/3rd as strong as Earth's field.","Number of Moons":"27","Gravity":"8.87 m/s²","Mass":"8.681 × 10^25 kg",
         "Diameter":"50,724 km","Orbital Period":"84 years","Rotational period":"0d 17h 14m","Life":"No life","Atmosphere":"Uranus' atmosphere is mostly hydrogen and helium, with a small amount of methane and traces of water and ammonia",
         "Rings":"Have rings but very thin"}


Neptune = {"Distance from Sun":"4.4729 billion km","Distance from Earth":"4.3327 billion km ","Location":"8th planet in non habitable zone",
         "Planet type":"Gas gaint","Spin":"Counter Clockwise","Surface temperature":"No any solid surface but it is too cold planet",
         "Magnetic feild":" 27 times more powerfull than that of Earth","Number of Moons":"14","Gravity":"11.15 m/s²","Mass":"1.024 × 10^26 kg",
         "Diameter":"49 244 kilometers","Orbital Period":"165 years","Rotational period":"0d 16h 6m","Life":"No life","Atmosphere":"Neptune's atmosphere is made up mostly of hydrogen and helium with just a little bit of methane.",
         "Rings":"Have rings but very thin"}
planet=input("Enter the planet you want to get information:")
list=[Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune]
if planet in list:
    for key,value in planet:
        print("{key},{value}")
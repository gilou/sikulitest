Invoke-WebRequest https://launchpad.net/sikuli/sikulix/1.1.1/+download/sikulixsetup-1.1.1.jar -OutFile C:\Temp\sikulixsetup-1.1.1.jar
java -jar "C:\Temp\sikulixsetup-1.1.1.jar" 1.1
cd C:\Temp
git clone https://github.com/gilou/sikulitest.git windows_adobe.sikuli

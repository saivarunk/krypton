# Installation

The krypton module can be installed from the PyPI repository using
```bash
pip install krypton-ml
```

Once the package is installed, you can start the Krypton Model server using Krypton CLI
```bash
krypton server
```

- For the first time, the krypton model server would try to create directory at ```~/krypton/models``` by default.
- This will vary depending upon the kind of os you are using.

The location can look like these for each operating system:

- Mac:  ```/Users/<user_name>/krypton/models```
- Linux: ```/home/<user_name>/krypton/models```
- Windows: ```C:\Users\<user_name>\krypton\models```

This path can be modified to a custom location by setting ```KRYPTON_APP_ROOT``` value to any valid 
location where you want krypton server to setup the ```models``` directory.

The server would be started at ```PORT``` 7000 by default, and it can be accessed at ```http://localhost:7000```

![Krypton CLI](assets/krypton_cli.png)
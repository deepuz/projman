# projman

The python cli tool that is used to generate a project folder structure based on the input *yaml* file structure
The path to the *yaml* file needs to be stored in **PROJMAN_TEMPLATE** environment variable or optionally passed as parameter using **-f**
The project structure will be generated in the the location specified in **PROJMAN_LOCATION** environment variable. If the environment variable is not set,the project folders will be created in the current working directory 

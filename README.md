# Minecraft_Server_Controller
A program for administering and managing multiple Minecraft servers on the same computer easily

## Requirements
`Minecraft_Server_Controller` requires python 3.8 or higher.

`Minecraft_Server_Controller` requires the use on mcipc which is being used under GNU General Public License and was originally created by github.com user conqp and can be found here https://github.com/conqp/mcipc.

## Usage
the program is entirely used throught the `GUI.py` file in the repositpory. Usage does require basic knowledege of administering a minecraft server and to have set up the RCON protocol on which ever server you wish to manage. This can be done by editing the `server.properties` file in the directory where you have installed your files. You also need to have the server to be usign a `serverstart.bat` to start your server. I have provided an example one if you don't know how to create one, you will need to change the `.jar` file if you decide to use that one.

### Add server
To add a server:
* Click the `add server` button on the main page
* Fill out the requsted information
* Click `add server` at the bottom. You will see a message that the server was added successfully

### Manage Servers
To manage a server:
* CLick `Manage Servers`
* if you just added a server click `Refresh Servers`
* select the Server name from the drop down box
* Use any of the commands below

#### Commands
* `Delete Server` removes the currently selected server from the program
* `Start\Stop Server` Starts or stops the server. Due to limitations in Minecraft you can only stop once the server is fully loaded
* `Exefcute Command` attempts to execute whatever is typed in the box to it's left. Note: commands do NOT need a '/' to work
* `Set Time to Day/Night` Sets server time to day or night
* `Peaceful/Easy/Normal/Hard` sets server difficuty
* `Clear/Rainy Weather` Changes weatehr on server
* `Teleport` Teleports user from the first text box to user in the second text box
* `OP User` makes user an Op, user must be online

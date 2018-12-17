#Android Compabilities Test Suite
---
*This [brand](https://bitbucket.org/misfitwearablesinc/qa-wearos/src/cts/) support run [CTS suite](https://source.android.com/compatibility/cts) and update result to googleshet automatically.*

### How do I get set up? 
* Setup ubuntu OS
* Install [java-jdk](http://tipsonubuntu.com/2016/07/31/install-oracle-java-8-9-ubuntu-16-04-linux-mint-18/) (recommend use java 8)
  ```sh
  $ sudo apt update
  $ sudo apt install oracle-java8-installer
  ```
* Install [android-sdk](https://developer.android.com/studio/)
* Setup **JAVA_HOME** on *~/.bashrc*
* Setup **ANDROID_HOME** on *~/.bashrc*
* Add **JAVA_HOME** and **ANDROID_HOME**  into **PATH**
    * Insert more lines below into *~/.bashrc*
  
    ```sh
    export JAVA_HOME=/usr/lib/jvm/java-8-oracle
    export PATH=$PATH:$JAVA_HOME/bin
    export ANDROID_HOME=/home/admin1/Android/Sdk
    export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/28.0.3:/var/lib/jenkins

    ```
* Install python (2 or 3)
* Install pip packages:
    ```sh
        $ pip install --upgrade google-api-python-client oauth2client  
        $ pip install subprocess pygsheets
    ```

* Download [CTS suite](https://dl.google.com/dl/android/cts/android-cts-8.1_r9-linux_x86-arm.zip) and put on CTS_DIR= '/home/admin1/Documents/android-cts'

###  How to run this

```sh 
$ python readGoogleSheet.py
```

### How it work
* Step 1: Read testplan on googlesheet
* Step 2: run the modules that have used = 'y' and execute != 'Done'
* Step 3: read all test_result.xml
* Step 4: centralize report to csv file
* Step 5: update google sheet result
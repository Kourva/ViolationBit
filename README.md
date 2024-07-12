<div align="center">
  <img width=400 align="right" src="https://github.com/kozyol/ViolationBit/assets/118578799/ffbff4e9-a1a6-4f23-a4b6-f9207213943d" />
  <h3 align="left">Violation Bit</h3>
  <p align="left">Violation bit simulator using Manchester II (BiPhase-L)</p>
  <p align="left">G. E. Thomas convention</p>
</div>

<br>

<h3>‡ Installation</h3> 

+ Clone repository
    ```bash
    git clone https://github.com/kozyol/ViolationBit
    ```

+ Navigate to ViolationBit
    ```bash
    cd ViolationBit
    ```
+ Make virtual environment and activate it
    ```bash
    virtualenv venv && source venv/bin/activate
    ```
+ Install requirements
   ```bash
   pip install -r requirements.txt
   ```
+ Run simulation
   ```bash
   python main.py -x "-1" -n "2" -d "0110 00110 10"
   ```
   Where:
   - **-x** is minimum voltage
   - **-n** is maximum voltage
   - **-d** is the data
   - **-h** to see usage (You will get error if you dont specify the arguments)

     

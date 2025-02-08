# medimeet
A Mini Telehealth Appointment System

<h1>Let's start with the architecture and schema design:</h1><br/>

So, Database Name --> `medimeet_db` and it contain mainly 4 tables:<br />

![Screenshot 2025-02-08 at 6 00 49 PM](https://github.com/user-attachments/assets/840c6ee6-6bb9-48fb-8c9b-a3ecf6a3b3c7)

<ol><li><h2>
  
First of all `patients` table</h2></li><br/>
It contain ```id```, ```fname```, ```lname```, ```phone```, ```password```, ```age```<br/>
  
![Screenshot 2025-02-08 at 6 07 44 PM](https://github.com/user-attachments/assets/b36e793f-1a04-4abb-9924-e711105992ac)

So, patient can register themselves and entry will be created inside this table.<br/>
> In ideal scenario, directly saving passwords is a huge risk, so it is recommended to save it as hash. (Which i havn't used, as this is a mini project and to complete the project before deadline, i ignored it.)<br/>

<li><h2>
  
Second ```doctors``` table</h2></li><br/>
It contain ```id```, ```fname```, ```lname```, ```specialty```, ```experience```<br/>

![Screenshot 2025-02-08 at 6 14 03 PM](https://github.com/user-attachments/assets/ade1a616-d088-4007-8b89-0984f7faa29e)

<li><h2>
  
Third ```slots``` table</h2></li><br/>
It contain ```id```, ```doctor_id```, ```date```, ```start_time```, ```start_time```<br/>

![Screenshot 2025-02-08 at 6 16 45 PM](https://github.com/user-attachments/assets/72c01275-f246-4210-a54e-36b617d60e1e)

The Slot table is designed specifically to work for this project.
> Ideally, I would have implemented a dynamic slotting system, where slots are generated based on the doctor's available timings and the number of possible splits. Instead of pre-saving all slots in the table, only the booked slots would be stored when a user schedules an appointment.

<li><h2>
  
Fourth ```appointments``` table</h2></li><br/>
It contain ```id```, ```doctor_id```, ```patient_id```, ```slot_id```, ```current_status```<br/>

![Screenshot 2025-02-08 at 6 26 14 PM](https://github.com/user-attachments/assets/0ae18c37-5001-4470-88d8-3a8999363c6c)

>Ideally this table should also contain the payment done or not etc. but to make it simple and working i used this.
</ol>



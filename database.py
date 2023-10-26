import sqlite3

connection=sqlite3.connect("questions.db")

cursor = connection.cursor()



print("TWO MARKS------------------------------------")

cursor.execute("create table Two_marks(Q_id integer PRIMARY KEY,Question text,Unit integer,Level integer,Importance integer)")

cursor.execute("insert into Two_marks values (1,'Differentiate Circuit-switched networks and Packet-switched networks.',1,1,1)")

cursor.execute("insert into Two_marks values (2,'How are the subgroups of OSI model layers segregated by their functions ?',1,0,2)")

cursor.execute("insert into Two_marks values (3,'Define flow control.',1,1,3)")

cursor.execute("insert into Two_marks values (4,'What is transmission media ? Give example.',1,1,4)")

cursor.execute("insert into Two_marks values (5,'Write the parameters used to measure network perfromance.',1,1,5)")

cursor.execute("insert into Two_marks values (6,'Distinguish betweeen packet switched and circuit switched networks.',1,1,6)")

cursor.execute("insert into Two_marks values (7,'What is meant by bit stuffing ? Give an example.',1,1,7)")

cursor.execute("insert into Two_marks values (8,'Write down the requirements to build a computer network.',1,1,8)")

cursor.execute("insert into Two_marks values (9,'List the metrics that influence the performance of computer network.',1,1,9)")

cursor.execute("insert into Two_marks values (10,'How number of duplex mode link is calculated for mesh topology ?',1,0,10)")

cursor.execute("insert into Two_marks values (11,'What is URL ?',1,1,11)") 

cursor.execute("insert into Two_marks values (12,'Define the term : Bandwidth and Latency.',1,1,12)")

cursor.execute("insert into Two_marks values (13,'Compare Byte-Oriented versus Bit-Oriented protocol.',1,1,13)")

cursor.execute("insert into Two_marks values (14,'Which layer implements the node to node channel connection in OSI layered architecture ?',1,0,14)")

cursor.execute("insert into Two_marks values (15,'Give the syntax to create and initialize an array in Java.Write a Java program to find an element position in integer array',1,0,15)")

cursor.execute("insert into Two_marks values (16,'State the ways in which string comparison can mplemented in Java',1,0,16)")

cursor.execute("insert into Two_marks values (17,'Outline the need for switching.',1,1,17)")

cursor.execute("insert into Two_marks values (18,'List out the functions of the Data Link Layer.',2,1,1)")

cursor.execute("insert into Two_marks values (19,'Distinguish between a point-to-point link and a broadcast link.',2,1,2)")

cursor.execute("insert into Two_marks values (20,'Outline the use of Cyclic Redundancy Check.',2,1,3)")

cursor.execute("insert into Two_marks values (21,'Define hidden node problem.',2,1,4)")

cursor.execute("insert into Two_marks values (22,'What is Bluetooth ?',2,1,5)")

cursor.execute("insert into Two_marks values (23,'State the functions of bridges.',2,1,6)")

cursor.execute("insert into Two_marks values (24,'When an ICMP redirect message used ?',2,0,7)")

cursor.execute("insert into Two_marks values (25,'Define 802.11.',2,1,8)")

cursor.execute("insert into Two_marks values (26,'What do you mean by switching ?',2,1,9)")

cursor.execute("insert into Two_marks values (27,'What is the need for fragmentation ?',2,0,10)")

cursor.execute("insert into Two_marks values (28,'Draw the frame format of Ethernet.',2,1,11)")

cursor.execute("insert into Two_marks values (29,'Highlight the characteristics of datagram networks.',2,1,12)")

cursor.execute("insert into Two_marks values (30,'What details are provided by DHCP other than IP address ?',2,0,13)")

cursor.execute("insert into Two_marks values (31,'What is meant by a web server ? Give two examples.',2,1,14)")

cursor.execute("insert into Two_marks values (32,'Mention any four advantages of CSS.',2,1,15)")

cursor.execute("insert into Two_marks values (33,'Why IPv6 is preferred over IPv4 ?',3,0,1)")

cursor.execute("insert into Two_marks values (34,'what is DHCP ?',3,1,2)")

cursor.execute("insert into Two_marks values (35,'present an outline of IPv6 addressing.',3,1,3)")

cursor.execute("insert into Two_marks values (36,'Expand ICMP and write the function.',3,1,4)")

cursor.execute("insert into Two_marks values (37,'Write the types of connecting devices in internetworking.',3,1,5)")

cursor.execute("insert into Two_marks values (38,'Hoe do routers differentiate the incoming unicast,multicast and broadcast IP packets.',3,0,6)")

cursor.execute("insert into Two_marks values (39,'Why is IPv4 to IPv6 transition required ?',3,0,7)")

cursor.execute("insert into Two_marks values (40,'What are the benefits of Open Shortest Path First (OSPF) protocol ?',3,1,8)")

cursor.execute("insert into Two_marks values (41,'What is multicast routing ?',3,1,9)")

cursor.execute("insert into Two_marks values (42,'What are the two major mechanisms defined to help transition from IPv4 to IPv6 ?',3,0,10)")

cursor.execute("insert into Two_marks values (43,'Differentiate between forwarding table and routing table.',3,1,11)")

cursor.execute("insert into Two_marks values (44,'What is Border Gateway Protocol (BGP) ?',3,1,12)")

cursor.execute("insert into Two_marks values (45,'List the two factors that affect the performance ofa network switch.',3,1,13)")

cursor.execute("insert into Two_marks values (46,'List any four mathods of the Java Script Date object.',3,1,14)")

cursor.execute("insert into Two_marks values (47,'State four advantages of JSP over JavaServlets.',3,1,15)")

cursor.execute("insert into Two_marks values (48,'how congestion occurs in a network',4,0,1)")

cursor.execute("insert into Two_marks values (49,'What happens in the three way handshaking between any two devices ?',4,1,2)")

cursor.execute("insert into Two_marks values (50,'What is piggybacking.',4,1,3)")

cursor.execute("insert into Two_marks values (51,'outline stop-and-wait ARQ mecahnism.',4,1,4)")

cursor.execute("insert into Two_marks values (52,'What do you mean by slow start in TCP congestion ?',4,1,5)")

cursor.execute("insert into Two_marks values (53,'List the phases used in TCP congestion.',4,1,6)")

cursor.execute("insert into Two_marks values (54,'List the advantages of connection oriented services over connectionless services.',4,1,7)")

cursor.execute("insert into Two_marks values (55,'How do fast retransmit mechanism of TCP works ?',4,0,8)")

cursor.execute("insert into Two_marks values (56,'What are the services provided by Transport Layer protocol ?',4,1,9)")

cursor.execute("insert into Two_marks values (57,'Define congestion control.',4,1,10)")

cursor.execute("insert into Two_marks values (58,'Hoe does UDP address flow control mechanism ?',4,0,11)")

cursor.execute("insert into Two_marks values (59,'State the purpose of service model.',4,1,12)")

cursor.execute("insert into Two_marks values (60,'Compare flow control versus congestion control.',4,1,13)")

cursor.execute("insert into Two_marks values (61,'Define QoS.',4,1,14)")

cursor.execute("insert into Two_marks values (62,'Why PHP is called a loosely typed language ?',4,0,15)")

cursor.execute("insert into Two_marks values (63,'Define XML namespace.',4,1,16)")

cursor.execute("insert into Two_marks values (64,'Define FTP.',5,1,1)")

cursor.execute("insert into Two_marks values (65,'What is the difference between IMAP and POP ?',5,1,2)")

cursor.execute("insert into Two_marks values (66,'What is HTTP ?',5,1,3)")

cursor.execute("insert into Two_marks values (67,'Present an outline of SSH.',5,1,4)")

cursor.execute("insert into Two_marks values (68,'Define URL.',5,1,5)")

cursor.execute("insert into Two_marks values (69,'Mention the different levels in domain name space.',5,0,6)")

cursor.execute("insert into Two_marks values (70,'State the usage of conditional get in HTTP.',5,1,7)")

cursor.execute("insert into Two_marks values (71,'Present the information contained in a DNS resource record.',5,0,8)")

cursor.execute("insert into Two_marks values (72,'Write the uses of HTTP.',5,1,9)")

cursor.execute("insert into Two_marks values (73,'What is DNS ?',5,1,10)")

cursor.execute("insert into Two_marks values (74,'Draw the scenario of Electronic mail.',5,1,11)")

cursor.execute("insert into Two_marks values (75,'Draw a diagram that illustrate tunneling strategy.',5,1,12)")

cursor.execute("insert into Two_marks values (76,'Write the use of Hyper Text Transfer Protocol (HTTP).',5,1,13)")

cursor.execute("insert into Two_marks values (77,'What do you mean by Web Services Description Language (WSDL)',5,1,14)")

cursor.execute("insert into Two_marks values (78,'What is the use of SNMP protocol in a network ?',5,1,15)")

cursor.execute("insert into Two_marks values (79,'What is AJAX call back function ?',5,1,16)")

cursor.execute("insert into Two_marks values (80,'State the types of Webservices.',5,1,17)")




for row in cursor.execute("select * from Two_marks"):
    print(row)


print("TWELVE MARKS------------------------------")



cursor.execute("create table Twelve_marks (Q_id integer PRIMARY KEY,Question text,Unit integer,Level integer,Importance integer)")

cursor.execute("insert into Twelve_marks values (1,'Draw the OSI-ISO architecture and outline the functions performed by each layer.',1,1,1)")

cursor.execute("insert into Twelve_marks values (2,'Describe Circuit-Switching and packet-Switching with an example.',1,0,2)")

cursor.execute("insert into Twelve_marks values (3,'Explain any two error detection mechanism in detail.',1,1,3)")

cursor.execute("insert into Twelve_marks values (4,'Explain in detail about : (1) HDLC (2) PPP .',1,1,4)")

cursor.execute("insert into Twelve_marks values (5,'Discuss the different ways to address the framing problem.',1,0,5)")

cursor.execute("insert into Twelve_marks values (6,'Explain with relevant diagram the functions of physical and data link layer.',1,1,6)")

cursor.execute("insert into Twelve_marks values (7,'Discuss your understanding of Bit Oriented Protocol namely HDLC.',1,0,7)")

cursor.execute("insert into Twelve_marks values (8,'Discuss the approaches used for error detection in networking.',1,0,1)")

cursor.execute("insert into Twelve_marks values (9,'Explain in detail about the error and flow control mechanisms employed at data link layer.',2,0,1)")

cursor.execute("insert into Twelve_marks values (10,'Give the comparison between different wireless technologies ? Enumerate 802.11 protocol stack in detail.',2,1,2)")

cursor.execute("insert into Twelve_marks values (11,'Write a short note on : (1) DHCP (2) ICMP',2,1,3)")

cursor.execute("insert into Twelve_marks values (12,'Outline the working principle of Bluetooth technology.',2,1,4)")

cursor.execute("insert into Twelve_marks values (13,'Explain the architecture of IEEE 802.11 Wireless LAN.',2,1,5)")

cursor.execute("insert into Twelve_marks values (14,'What are the different routing algorithms ? List out their pros and cons.',3,0,1)")

cursor.execute("insert into Twelve_marks values (15,'With a neat diagram explain Distance vector routing protocol.',3,1,2)")

cursor.execute("insert into Twelve_marks values (16,'Explain about IPv6 ? Compare IPv4 and IPv6.',3,1,3)")

cursor.execute("insert into Twelve_marks values (17,'Explain the working of Protocol Independent Multi-cast (PIM) in deatil.',3,1,4)")

cursor.execute("insert into Twelve_marks values (18,'discuss the fundamentals and advantages of open shortest path first protocol',3,0,5)")

cursor.execute("insert into Twelve_marks values (19,'With an example, explain the function of link state routing protocol.',3,0,6)")

cursor.execute("insert into Twelve_marks values (20,'Elaborate on multicast routing protocol.',3,0,7)")

cursor.execute("insert into Twelve_marks values (21,'What are the two broad categories of Congestion Control mechanisms ? Briefly explain all the techniques.',4,1,1)")

cursor.execute("insert into Twelve_marks values (22,'Furnish the packet format of Stream Control Transmission Protocol with its fields.How are the data transferred with four way handshaking ?',4,0,2)")

cursor.execute("insert into Twelve_marks values (23,'Define UDP, Discuss the operations of UDP. Explain UDP checksum with one example.',4,0,3)")

cursor.execute("insert into Twelve_marks values (24,'Explain in detail the various TCP congestion control mechanisms.',4,0,4)")

cursor.execute("insert into Twelve_marks values (25,'Explain the congestion control techniques used to improve QOS of the computer network.',4,1,5)")

cursor.execute("insert into Twelve_marks values (26,'Write a detailed note on congestion avoidance mechanisms used in TCP.',4,1,6)")

cursor.execute("insert into Twelve_marks values (27,'What is the format of an email ? Explain the architecture of a mailing system.',5,1,1)")

cursor.execute("insert into Twelve_marks values (28,'Does the SSL protocol need the services of a certificate authority ? Explain your answer.',5,0,2)")

cursor.execute("insert into Twelve_marks values (29,'Explain in detail about Web service architecture.',5,1,3)")

cursor.execute("insert into Twelve_marks values (30,'Discuss the working of Email in detail.',5,1,4)")

cursor.execute("insert into Twelve_marks values (31,'Discuss in deatail about HTTP operation.',5,1,5)")

cursor.execute("insert into Twelve_marks values (32,'Write your understanding on File Transfer Protocol.',5,0,6)")






for row in cursor.execute("select * from Twelve_marks"):
    print(row)




cursor.close()

connection.commit()


connection.close()




 # DNS Spooffer Script : 
 
 - Create Target-Intercepted Packets Queue Using IPTables .  
    * iptables -I FORWARD -j NFQUEUE --queue-num 0 
     * -I : Specify which network chain to IPTables I want to modify here is "Forward-chain" .
     * -j : Specify queue type for IPTables here is "Net-filter queue" . 
     * -queue-num : Specify queue ID number to identify the queue . 
    
    * iptables --flush : Delete packets queue from IPTables, make sure to delete it when done with the attack . 
    
 - Use NetFilterQueue module to access and modify packets in the queue . 
   - QueueObject = netfilterqueue.NetfilterQueue() 
    * Create net filter queue to deal with intercepted packets queue .  
   
   - QueueObject.bind(PacketsQueueNumber, CallBackFunction) .
     * PacketsQueueNumber : The packet --queue-num I specified in the IPTables . 
     * CallBackFunction : Function to be called for each packet in the queue same as prn of scapy.sniff .

  - QueueObject.run()
    * Run the queue to work using this function . 
    * Now packets will be intercepted and stored in the queue without forwarding it to the target . 
  
  - In call back function, InterceptedPackets.accept() 
    * Accept and forward intercepted packets to the target . 

 - In call back function, InterceptedPackets.drop() 
   * Drop intercepted packets reached from the target to cut the connection .  

 - In call back function, InterceptedPackets.repeat() 
   * Repeat the intercepted packets over and over again . 

 - In call back function, InterceptedPackets.get_payload() 
   * Show the intercepted packets content and fields .  
   * All data will be in the bytes format, so I need to convert all intercepted packet to scapy packets format . 
 
 - scapy.IP(InterceptedPackets.get_payload()) 
   * Convert intercepted packets to scapy to be able to deal with its content and fields .  

 - After modify forged DNS response | request, switch over the original part (.qd | .an) in the original response | request . 

 - Must modify answers count field in the original response | request packet to match the number of responses | requests I want to redirect to the target . 

 - Must delete (len "Length" & chksum "Checksum") fields from IP & UDP packets part and let scapy re-calculate them . 

 - After modifications done re-set the payload into to original intercepted packet . 
   * InterceptedPackets.set_payload(bytes(ScapyEditionPacket)) . 

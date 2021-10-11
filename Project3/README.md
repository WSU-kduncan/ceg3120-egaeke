PART 1:
    1. A VPC serves as a sort of private cloud hosted within the public cloud. In this case, it is hosted by AWS.
    2. A subnet is a range of IP addresses in the VPC. Since it is a subset of the VPC, it can have additional levels of security.
    3. An internet gateway is a way that allows for communications between the VPC and the internet. It performs NAT for instances that have been assigned IPv4 addresses.
    4. It contains the rules (routes) that determines where network traffic from the VPC subnet or gateway is directed.
    5. Security groups act as a firewall for your instnace by controlling inbound and outbound traffic. You can determine what traffic can enter or exit by adding rules to the security group.

PART 2:
    1. N/A
    2. When creating the instance, I was able to choose my VPC under the configure tab of the instance creation.
    3. After creating the volume, I clicked "Actions" and chose "Attach volume" and then attached it to my instance. I had some issues with this because it created in zone us-east-1a and my VPC was in us-east-1d.
    4. Yes, I auto-assigned it because I wasn't entirely sure what to put and the default ended up working out.
    5. I navigated to the instance summary and went to the tags tab. I added a new tag with the necessary information.
    6. I navigated to the instance menu and selected "Actions" -> "Security" -> "Change security groups" and then removed the default group and added mine.
    7. I navigated to the elastic ip tab and allocated a new ip address, then selected associate elastic ip address and added it to my instance.
    8. N/A
    9. 
    10. N/A
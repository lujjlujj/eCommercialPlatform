#Enable Instrument Log
* Enable Instrument Log in Process Admin with TW_Admin Right.
* Execute following command line:
   /opt/bpm80/java/bin/java -Xmx1024M -cp /opt/bpm80/BPM/Lombardi/lib/svrcoreclnt.jar com.lombardisoftware.instrumentation.log.tools.NonXMLDump /appvol/BPM80/TPSBPM01HK.AppTarget.tkqp1csmwas80.0/waslog/logs/inst006.dat -dumplfOver 999999 -truncatelfOver 999999 > /tmp/inst006_deployment.txt
* Execute grep 'period [0-9][0-9][0-9]' inst006_deployment.txt > inst006_deployment_analysis_1.txt

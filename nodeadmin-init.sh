#! /bin/sh
### BEGIN INIT INFO
# Provides:          nodeadmin-init.sh
# Required-Start:    
# Required-Stop:     
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Starting Admin Panel for MySQL
# Description:       Nodeadmin is a PHPmyAdmin like interface for manage MySQL Databases
### END INIT INFO



#Switch case fuer den ersten Parameter
case "$1" in
    start)
		#action for start
        echo "start nodeadmin-init.sh"
		/usr/local/lib/node_modules/pm2/bin/pm2 start /home/pi/nodeadmin/nodeadmin.js
        ;;
		
    stop)
		#Action for stop
        echo "stop nodeadmin-init.sh"
		/usr/local/lib/node_modules/pm2/bin/pm2 stop /home/pi/nodeadmin/nodeadmin.js
        ;;
		
    restart)
		#Action for restart
        echo "restart nodeadmin-init.sh"
		/usr/local/lib/node_modules/pm2/bin/pm2 start /home/pi/nodeadmin/nodeadmin.js
        ;;
	*)
		#Default action if no start|stop|restart is called
		echo "(start|stop|restart)"
		/usr/local/lib/node_modules/pm2/bin/pm2 start /home/pi/nodeadmin/nodeadmin.js
		;;
esac

exit 0

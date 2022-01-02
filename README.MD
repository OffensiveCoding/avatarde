edit config file: /etc/tor/torrc

uncomment:
	ControlPort 9051
	HashedControlPassword 16:50940E5B2C8C1963602F6E14F1E184BA1F9245F72936F5BAC4C149>
	CookieAuthentication 1

add to end of file:
	HTTPTunnelPort 9080


sudo service tor restart

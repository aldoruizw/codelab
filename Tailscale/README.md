# Tailscale Exit Node on Raspberry Pi

This guide explains how to configure a Raspberry Pi as a [Tailscale](https://tailscale.com) **exit node**, so all your devices can securely route their internet traffic through it.

---

## 📦 Requirements
- Raspberry Pi (Pi 4 or newer recommended)
- Raspberry Pi OS / Linux installed
- A [Tailscale account](https://login.tailscale.com/start) (free plan works)

---

## 🚀 Installation & Setup

### 1. Install Tailscale
```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

Log in with your Tailscale account when prompted.

---

### 2. Enable Exit Node on the Pi
```bash
sudo tailscale up --advertise-exit-node
```

---

### 3. Enable IP Forwarding
Exit nodes require IP forwarding to send traffic correctly.

Enable for the current session:
```bash
sudo sysctl -w net.ipv4.ip_forward=1
sudo sysctl -w net.ipv6.conf.all.forwarding=1
```

Make it permanent:
```bash
echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf
echo "net.ipv6.conf.all.forwarding=1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

---

### 4. Approve Exit Node in Admin Console
1. Open [Tailscale admin console](https://login.tailscale.com/admin)  
2. Go to **Machines** → select your Raspberry Pi  
3. Click **Edit route settings**  
4. Enable **Use as exit node**

---

### 5. Use the Exit Node from Another Device

Find your Pi’s Tailscale IP:
```bash
tailscale ip -4
```

Connect through it:
```bash
sudo tailscale up --exit-node=<PI_TAILSCALE_IP>
```

Or, in the Tailscale app:
- Go to **Settings → Exit node**
- Select your Raspberry Pi

---

## ✅ Done!
Your Raspberry Pi is now a secure exit node.  
All your devices can route their internet traffic through it using Tailscale.

---

## 🔧 Optional: Advertise LAN Subnet
If you also want to reach LAN devices (e.g., `192.168.1.x`) behind your Pi:

```bash
sudo tailscale up --advertise-exit-node --advertise-routes=192.168.1.0/24
```

Then approve the route in the Tailscale admin console.

# Linux Help
This is a quick guide that is intended to help newby's with installing, uninstalling,
and just working with Linux in general. This document should serve as a reference
for other resources that will help with Linux.

## Installing Linux
First we must cover how to actually install Linux on your current machine. This guide
will work for if you want to dual boot Linux or if you want to run it as your primary OS.

### Download Links
You can first download any distro you want from [This Website](https://www.linux.org/pages/download/).

### Bootable Drive Creator
After you have downloaded the .iso file for the distro that you want, you need
to create a bootable drive with that .iso file. I use [Balena Etcher](https://www.balena.io/etcher/)
as my tool but feel free to use whatever you'd like. Etcher works for both MacOS and Windows.

### Booting Into ISO
Once you have created a bootable drive with Etcher, you can now proceed to booting into your .iso file. To do this, restart your computer and look up according to your make and model
what button(s) you have to push while your computer is restarting. For MacOS you can boot into
an .iso by holding the option key on start up. On some Windows machines it is F11 but it could be
different for yours.

### Follow On Screen Prompts
At this point the set up is pretty strait forward. You will need to do what the on screen
prompts ask you to do in order to install your distro of Linux.

### Choosing OS on Boot
Now you may be wondering how do you boot into your new OS? It's pretty simple. When your
machine is starting, press/ hold the same button that you had to hold to boot into your
.iso. This will allow you to choose between your main OS or Linux. If you want to boot into
Linux by default, you will have to boot into your BIOS and choose what your default OS is. This
is different for almost every make and model.

## Uninstalling Linux (Dual Boot Setup)
Before we get into using Linux I want to cover how to remove Linux if you need to. For starters,
the first thing that you need to do is delete the partitions from from your main OS.
Once the partitions have been deleted you need to delete GRUB (Grand Unified Bootloader).
To delete GRUB from Windows to do the following: (Quotes are used to reference other generic credentials in context)
- Run: cmd.exe (With Admin Privileges)
- Run: diskpart
- Run: list disk
- Run: sel disk "x"
- Run: list vol
- Run: sel vol "y" (Where y is the SYSTEM Volume)
- Run: assign letter=Z:
- Run: exit
(Make sure to remain in cmd)
- Run: Z:
- Run: dir
(You should see a directory titled EFI)
- Run: cd EFI
- Run: dir
- Run: rmdir /S "distro name"
- Reboot your system

To delete GRUB from MacOS, open terminal and do the following: (Quotes are used to reference other generic credentials in context)
- Run: mkdir mnt
- Run: sudo mount -t msdos /dev/disk0s1 mnt
- Run: cd mnt/EFI/
- Run: sudo rm -rf ubuntu
- Run: sudo reboot

At this point you should successfully have been able to remove GRUB from either
Windows or MacOS. With this out of the way we can move on to how to begin using
Linux.

BREVEDIR	= ../..
CPPFLAGS	+= -I..
CC              = i686-pc-mingw32-gcc
CXX             = i686-pc-mingw32-g++

all: cSample_plugin.o c++Sample_plugin.o

cSample_plugin.o: cSample.o $(BREVEDIR)/lib/breveIDEPlugin.lib
	$(CXX) $(CPPFLAGS) -shared -o $@ cSample.o $(BREVEDIR)/lib/breveIDEPlugin.lib 

c++Sample_plugin.o: c++Sample.o $(BREVEDIR)/lib/breveIDEPlugin.lib
	$(CXX) $(CPPFLAGS) -shared -o $@ c++Sample.o $(BREVEDIR)/lib/breveIDEPlugin.lib

clean:
	rm -f *.o

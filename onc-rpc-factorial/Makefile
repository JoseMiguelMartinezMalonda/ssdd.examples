# This is a template Makefile generated by rpcgen

# Parameters

CLIENT = factorial_client
SERVER = factorial_server

SOURCES_CLNT.c = factorial_client.c
SOURCES_CLNT.h =
SOURCES_SVC.c = factorial_server.c
SOURCES_SVC.h =
SOURCES.x = factorial.x

TARGETS_SVC.c = factorial_svc.c
TARGETS_CLNT.c = factorial_clnt.c
TARGETS = factorial_server factorial_client

OBJECTS_CLNT = $(SOURCES_CLNT.c:%.c=%.o) $(TARGETS_CLNT.c:%.c=%.o)
OBJECTS_SVC = $(SOURCES_SVC.c:%.c=%.o) $(TARGETS_SVC.c:%.c=%.o)
# Compiler flags

STUBS = factorial_clnt.c factorial_svc.c factorial.h *_xdr.c

CFLAGS += -g
LDLIBS += -lnsl
RPCGENFLAGS =

# Targets

all : $(CLIENT) $(SERVER)

$(TARGETS) : $(SOURCES.x)
	rpcgen $(RPCGENFLAGS) $(SOURCES.x)

$(OBJECTS_CLNT) : $(SOURCES_CLNT.c) $(SOURCES_CLNT.h) $(TARGETS_CLNT.c)

$(OBJECTS_SVC) : $(SOURCES_SVC.c) $(SOURCES_SVC.h) $(TARGETS_SVC.c)

$(CLIENT) : $(OBJECTS_CLNT)
	$(LINK.c) -o $(CLIENT) $(OBJECTS_CLNT) $(LDLIBS)

$(SERVER) : $(OBJECTS_SVC)
	$(LINK.c) -o $(SERVER) $(OBJECTS_SVC) $(LDLIBS)

$(TARGETS_CLNT.c): $(SOURCES.x)
	rpcgen $(RPCGENFLAGS) $(SOURCES.x)

clean:
	$(RM) core $(TARGETS) $(OBJECTS_CLNT) $(OBJECTS_SVC) $(CLIENT) $(SERVER) $(STUBS)
	$(RM) *~

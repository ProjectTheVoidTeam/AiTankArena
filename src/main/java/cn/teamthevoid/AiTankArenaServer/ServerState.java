package cn.teamthevoid.AiTankArenaServer;

import io.netty.channel.Channel;

import java.util.HashMap;

public class ServerState {
    private HashMap<Integer, Session> sessionMap = new HashMap<>();//sessionID -> Session

    //返回SessionID
    public int createGameSession() {
        var newGameSession = new Session();
        sessionMap.put(newGameSession.getID(), newGameSession);
        return newGameSession.getID();
    }

    public Session getGameSession(long sessionID) {
        return sessionMap.get(sessionID);
    }

    //返回PlayerID
    public long joinGameSession(long sessionID, Channel channel) {
        return sessionMap.get(sessionID).join(channel);
    }


}

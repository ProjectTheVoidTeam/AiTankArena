package cn.teamthevoid.AiTankArenaServer;

import cn.teamthevoid.AiTankArenaServer.game.Game;
import cn.teamthevoid.AiTankArenaServer.game.Player;
import cn.teamthevoid.AiTankArenaServer.game.factory.GameFactory;
import cn.teamthevoid.AiTankArenaServer.game.factory.PlayerFactory;
import io.netty.channel.Channel;
import io.netty.util.AttributeKey;

import java.util.HashMap;

public class Session extends UniqueIDEntity {
    static AttributeKey<Session> SESSION_KEY = AttributeKey.valueOf("session");
    static AttributeKey<Player> PLAYER_KEY = AttributeKey.valueOf("player");

    public Game game = GameFactory.getNewInstance();
    private HashMap<Player, Channel> channelMap = new HashMap<>();//playerid -> Channel

    public Session() {
    }

    //返回PlayerID
    public long join(Channel channel) {
        var newPlayer = PlayerFactory.getNewInstance();
        channel.attr(SESSION_KEY).set(this);
        channel.attr(PLAYER_KEY).set(newPlayer);
        this.channelMap.put(newPlayer, channel);
        this.game.join(newPlayer);
        return newPlayer.getID();
    }
}

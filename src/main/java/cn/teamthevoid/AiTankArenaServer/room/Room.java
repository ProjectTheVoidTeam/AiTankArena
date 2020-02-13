package cn.teamthevoid.AiTankArenaServer.room;

import cn.teamthevoid.AiTankArenaServer.UniqueIDEntity;
import cn.teamthevoid.AiTankArenaServer.game.Game;
import cn.teamthevoid.AiTankArenaServer.game.Player;
import cn.teamthevoid.AiTankArenaServer.game.factory.GameFactory;
import cn.teamthevoid.AiTankArenaServer.message.response.GameState;
import io.netty.channel.Channel;
import lombok.extern.slf4j.Slf4j;

import java.util.HashMap;

@Slf4j
public class Room extends UniqueIDEntity {

    public Game game = GameFactory.getNewInstance();
    public HashMap<Player, Channel> channelMap = new HashMap<>();//Player -> Channel


    public Room() {
    }

    //返回PlayerID
    public Integer join(Channel channel, Player newPlayer) {
        channel.attr(ServerState.ROOM).set(this);
        channel.attr(ServerState.PLAYER).set(newPlayer);
        this.channelMap.put(newPlayer, channel);
        this.game.join(newPlayer);
        log.info(newPlayer + " join room:" + this.getID());
        return newPlayer.getID();
    }


    public void start() {
        this.game.start();
    }

    public GameState getGameState() {
        return null;//TODO:将game.gamestate转换为message.gamestate
    }
}

package cn.teamthevoid.AiTankArenaServer.handler;

import cn.teamthevoid.AiTankArenaServer.room.ServerState;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.socket.SocketChannel;
import lombok.extern.slf4j.Slf4j;

@Slf4j
public class GameServerInitializer extends ChannelInitializer<SocketChannel> {
    ServerState serverState;

    public GameServerInitializer(ServerState serverState) {
        this.serverState = serverState;
    }

    @Override
    protected void initChannel(SocketChannel ch) throws Exception {

        ChannelPipeline pipeline = ch.pipeline();
        pipeline.addLast(new LoggingHandler())
                .addLast(new ServerInfoHandler().setServerState(serverState))
                .addLast(new JoinGameHandler().setServerState(serverState))
                .addLast(new DebugHandler().setServerState(serverState));
    }
}

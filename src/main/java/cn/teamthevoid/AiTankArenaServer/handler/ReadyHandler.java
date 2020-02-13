package cn.teamthevoid.AiTankArenaServer.handler;

import cn.teamthevoid.AiTankArenaServer.message.operation.Operation;
import cn.teamthevoid.AiTankArenaServer.message.operation.OperationType;
import cn.teamthevoid.AiTankArenaServer.message.response.Response;
import cn.teamthevoid.AiTankArenaServer.message.response.Status;
import io.netty.channel.ChannelHandlerContext;

public class ReadyHandler extends OperationInboundHandlerAdapter {
    @Override
    OperationType getOperationType() {
        return OperationType.READY;
    }

    @Override
    void channelRead(ChannelHandlerContext ctx, Operation operation) {
        var selfPlayer = serverState.getSelf(ctx.channel());
        var selfRoom = serverState.getMyRoom(ctx.channel());
        selfPlayer.isReady = true;
        var players = selfRoom.channelMap.keySet();
        boolean isAllReady = players
                .stream()
                .filter(it -> it.isReady)
                .count() == players.size();
        if (isAllReady)
            selfRoom.start();

        ctx.channel().writeAndFlush(
                Response
                        .newBuilder()
                        .setStatus(Status.OK)
                        .setGameState(selfRoom.getGameState())
                        .build()
        );


    }
}

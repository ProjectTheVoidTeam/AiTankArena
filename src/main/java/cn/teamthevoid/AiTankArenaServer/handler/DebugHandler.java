package cn.teamthevoid.AiTankArenaServer.handler;

import cn.teamthevoid.AiTankArenaServer.message.operation.Operation;
import cn.teamthevoid.AiTankArenaServer.message.operation.OperationType;
import cn.teamthevoid.AiTankArenaServer.message.response.Response;
import cn.teamthevoid.AiTankArenaServer.message.response.Status;
import io.netty.channel.ChannelHandlerContext;

public class DebugHandler extends OperationInboundHandlerAdapter {
    @Override
    OperationType getOperationType() {
        return OperationType.DEBUG;
    }

    @Override
    void channelRead(ChannelHandlerContext ctx, Operation operation) {
        serverState.getRoom(0).channelMap.forEach(((player, channel) -> {
            var response = Response
                    .newBuilder()
                    .setStatus(Status.OK)
                    .build();
            channel.writeAndFlush(response
            );
        }));
        ctx.channel().writeAndFlush(Response.newBuilder().setStatus(Status.OK).build());

    }
}

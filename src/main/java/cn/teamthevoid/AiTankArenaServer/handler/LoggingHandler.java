package cn.teamthevoid.AiTankArenaServer.handler;

import cn.teamthevoid.AiTankArenaServer.message.operation.Operation;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import lombok.extern.slf4j.Slf4j;

@Slf4j
public class LoggingHandler extends ChannelInboundHandlerAdapter {


    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        Operation operation = (Operation) msg;
        log.debug("\nNew Operation Request:\n" + operation.toString());
        ctx.fireChannelRead(msg);
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) { // (4)
        cause.printStackTrace();
        ctx.close();
    }

}

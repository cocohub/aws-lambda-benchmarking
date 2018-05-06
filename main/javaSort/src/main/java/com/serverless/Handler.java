package com.serverless;

import java.util.Collections;
import java.util.Map;
import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

import org.apache.log4j.BasicConfigurator;
import org.apache.log4j.Logger;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

public class Handler implements RequestHandler<Map<String, Object>, ApiGatewayResponse> {

	private static final Logger LOG = Logger.getLogger(Handler.class);

	@Override
	public ApiGatewayResponse handleRequest(Map<String, Object> input, Context context) {
		BasicConfigurator.configure();
        
        int max = 10;
        
        max = Integer.parseInt(input.get("queryStringParameters").toString().split("=")[1].replace("}", ""));
        
        int[] array = new int[max];
        
        for (int i = 0; i < max; i++) {
            array[i] = ThreadLocalRandom.current().nextInt(0, max);
        }
        
        Arrays.sort(array);

		LOG.info("received: " + input);
		Response responseBody = new Response(Arrays.toString(array), input);
		return ApiGatewayResponse.builder()
				.setStatusCode(200)
				.setObjectBody(responseBody)
				.setHeaders(Collections.singletonMap("X-Powered-By", "AWS Lambda & serverless"))
				.build();
	}
}

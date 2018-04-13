package com.serverless;

import java.util.Collections;
import java.util.Map;
import java.util.Arrays;

import org.apache.log4j.BasicConfigurator;
import org.apache.log4j.Logger;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

public class Handler implements RequestHandler<Map<String, Object>, ApiGatewayResponse> {

	private static final Logger LOG = Logger.getLogger(Handler.class);
    
	@Override
	public ApiGatewayResponse handleRequest(Map<String, Object> input, Context context) {
		BasicConfigurator.configure();
    
        int[] array = {435, 401, 385, 310, 195, 686, 343, 689, 32, 751, 800, 124, 856, 901, 375, 230, 922, 97, 456, 667, 300, 803, 582, 376, 255, 440, 928, 38, 870, 250, 466, 878, 180, 562, 106, 46, 964, 793, 105, 96, 951, 268, 470, 181, 92, 838, 863, 311, 195, 323, 902, 762, 628, 835, 652, 265, 581, 500, 414, 225, 238, 694, 511, 487, 471, 276, 814, 371, 433, 610, 386, 211, 613, 262, 579, 371, 876, 301, 316, 421, 35, 197, 73, 472, 744, 537, 507, 490, 827, 842, 298, 585, 464, 204, 529, 170, 820, 268, 224, 233, 849, 290, 343, 775, 952, 829, 732, 680, 455, 914, 689, 778, 343, 569, 64, 474, 306, 154, 928, 558, 116, 464, 550, 59, 234, 710, 653, 639, 387, 625, 789, 533, 20, 912, 820, 53, 891, 306, 766, 235, 143, 87, 729, 247, 581, 679, 844, 972, 835, 679, 945, 701, 415, 651, 481, 820, 345, 327, 250, 629, 6, 496, 917, 111, 932, 548, 54, 581, 477, 168, 346, 807, 154, 480, 456, 588, 863, 664, 831, 531, 594, 229, 500, 356, 37, 136, 442, 856, 958, 633, 656, 254, 61, 119, 954, 298, 305, 631, 979, 275, 997, 833, 369, 671, 64, 206, 585, 802, 669, 697, 168, 615, 855, 564, 912, 126, 426, 90, 374, 565, 197, 685, 610, 664, 785, 924, 642, 354, 300, 312, 669, 923, 714, 295, 450, 240, 166, 744, 358, 507, 128, 614, 107, 987, 240, 107, 527, 676, 421, 209, 596, 845, 86, 139, 917, 733, 640, 809, 181, 234, 393, 20, 694, 254, 589, 187, 691, 372, 428, 531, 339, 797, 957, 757, 124, 55, 247, 579, 931, 577, 576, 987, 200, 697, 842, 690, 246, 185, 377, 610, 376, 28, 162, 867, 560, 677, 757, 861, 804, 717, 728, 126, 581, 186, 701, 273, 376, 109, 323, 141, 911, 88, 68, 925, 78, 56, 40, 391, 757, 459, 84, 33, 762, 174, 465, 315, 469, 540, 354, 592, 230, 883, 700, 55, 838, 76, 373, 594, 654, 949, 843, 51, 602, 682, 153, 251, 46, 994, 661, 441, 579, 58, 818, 147, 800, 707, 442, 727, 451, 519, 299, 120, 291, 257, 404, 395, 842, 17, 984, 681, 955, 41, 531, 925, 807, 312, 965, 775, 456, 441, 659, 322, 487, 306, 840, 514, 118, 923, 238, 880, 633, 399, 719, 9, 832, 683, 808, 764, 29, 640, 38, 975, 405, 21, 263, 407, 309, 753, 57, 130, 364, 982, 570, 122, 97, 886, 917, 89, 428, 705, 760, 654, 283, 748, 403, 777, 205, 252, 718, 812, 134, 42, 793, 860, 145, 610, 651, 21, 39, 109, 586, 341, 462, 391, 302, 173, 170, 258, 608, 557, 496, 538, 904, 17, 987, 372, 521, 876, 608, 988, 448, 295, 189, 210, 575, 355, 443, 936, 888, 932, 580, 273, 589, 441, 969, 406, 328, 838, 819, 425, 73, 105, 894, 605, 248, 284, 963, 644, 110, 471, 111, 123, 419, 974, 206, 764, 124, 678, 62, 875, 427, 598, 925, 542, 559, 256, 847, 675, 292, 673, 244, 909, 299, 745, 217, 374, 532, 305, 114, 447, 863, 231, 756, 107, 975, 445, 271, 25, 163, 92, 151, 801, 454, 300, 564, 760, 631, 782, 936, 683, 18, 778, 21, 951, 623, 904, 957, 351, 737, 470, 370, 310, 905, 915, 213, 79, 628, 856, 91, 63, 67, 842, 590, 15, 653, 166, 628, 124, 916, 30, 740, 932, 237, 203, 980, 501, 68, 250, 681, 636, 465, 364, 369, 310, 443, 549, 654, 98, 462, 989, 594, 948, 122, 543, 918, 648, 589, 211, 780, 95, 659, 279, 329, 948, 22, 743, 476, 266, 952, 198, 376, 970, 542, 812, 199, 462, 955, 164, 28, 833, 726, 505, 875, 824, 866, 190, 724, 461, 925, 761, 130, 525, 650, 713, 649, 579, 257, 788, 507, 424, 66, 36, 55, 533, 247, 127, 31, 805, 140, 760, 61, 992, 908, 156, 78, 205, 204, 217, 820, 296, 339, 661, 283, 668, 524, 566, 920, 819, 178, 173, 855, 376, 41, 58, 717, 791, 469, 547, 155, 590, 820, 391, 899, 118, 221, 151, 454, 550, 246, 163, 149, 395, 589, 264, 308, 886, 219, 140, 841, 137, 773, 648, 106, 576, 650, 572, 3, 373, 323, 235, 720, 519, 586, 259, 5, 659, 360, 885, 925, 616, 373, 802, 627, 808, 451, 21, 95, 597, 620, 608, 842, 217, 639, 178, 598, 908, 772, 606, 87, 868, 315, 453, 856, 393, 339, 274, 917, 773, 10, 611, 438, 780, 688, 536, 769, 155, 880, 107, 182, 244, 434, 470, 187, 477, 95, 803, 436, 607, 240, 337, 624, 841, 745, 926, 856, 730, 663, 750, 18, 888, 481, 727, 623, 318, 119, 821, 701, 220, 323, 43, 729, 878, 243, 937, 714, 643, 166, 337, 645, 980, 250, 880, 162, 763, 661, 118, 433, 854, 403, 265, 714, 464, 860, 748, 572, 91, 173, 80, 247, 104, 581, 599, 304, 833, 63, 265, 840, 705, 364, 680, 681, 746, 713, 4, 135, 234, 215, 925, 878, 162, 178, 280, 677, 845, 629, 692, 698, 527, 127, 721, 382, 727, 136, 833, 394, 149, 579, 289, 714, 467, 282, 87, 145, 104, 337, 693, 605, 843, 963, 34, 75, 245, 11, 827, 49, 154, 426, 305, 544, 476, 371, 737, 324, 818, 803, 465, 378, 602, 569, 522, 61, 62, 441, 307, 16, 95, 170, 816, 111, 133, 438, 575, 269, 778, 409, 916, 379, 106, 561, 414, 713, 549, 340, 192, 510, 921, 815, 383, 629, 372, 211, 757, 266, 779, 66, 28, 671, 396, 941, 245, 247, 680, 713, 763, 12, 306, 793, 570, 758, 369, 21, 91, 394, 827, 842, 433, 617, 486, 821, 376, 766, 875, 565, 616, 34, 859, 915, 270, 420, 668, 417, 81, 958, 894, 526, 516, 123, 11, 104, 706, 387, 133, 167, 868, 867, 949, 900, 778, 925, 330, 852, 518, 540, 912, 540, 817, 917, 816, 399, 397, 658, 546, 211, 282, 420, 528, 304, 846, 550, 102};
        Arrays.sort(array);
        System.out.println(Arrays.toString(array));
        
		LOG.info("received: " + input);
		Response responseBody = new Response(Arrays.toString(array), input);
		return ApiGatewayResponse.builder()
				.setStatusCode(200)
				.setObjectBody(responseBody)
				.setHeaders(Collections.singletonMap("X-Powered-By", "AWS Lambda & serverless"))
				.build();
	}
}
